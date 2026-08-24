# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 389
- HTTP: 118 alive / 69 gold
- HTTPS: 45 alive / 15 gold
- SOCKS4: 164 alive / 153 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33249
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
