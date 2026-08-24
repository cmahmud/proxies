# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 384
- HTTP: 121 alive / 68 gold
- HTTPS: 50 alive / 13 gold
- SOCKS4: 187 alive / 151 gold
- SOCKS5: 193 alive / 152 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33227
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
