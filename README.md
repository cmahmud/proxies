# SyndProxy private pool

## Current pool

- Alive now: 654
- Gold now: 390
- HTTP: 160 alive / 65 gold
- HTTPS: 83 alive / 18 gold
- SOCKS4: 205 alive / 152 gold
- SOCKS5: 206 alive / 155 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25714
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
