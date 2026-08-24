# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 376
- HTTP: 147 alive / 68 gold
- HTTPS: 38 alive / 13 gold
- SOCKS4: 182 alive / 148 gold
- SOCKS5: 184 alive / 147 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33227
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
