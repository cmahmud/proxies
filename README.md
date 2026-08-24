# SyndProxy validated proxy pool

## Current pool

- Alive now: 543
- Gold now: 392
- HTTP: 127 alive / 58 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 205 alive / 165 gold

## Historical pool

- Discovered: 178292
- Ever alive: 33372
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
