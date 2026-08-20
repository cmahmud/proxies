# SyndProxy private pool

## Current pool

- Alive now: 761
- Gold now: 380
- HTTP: 191 alive / 73 gold
- HTTPS: 152 alive / 18 gold
- SOCKS4: 212 alive / 146 gold
- SOCKS5: 206 alive / 143 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26292
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
