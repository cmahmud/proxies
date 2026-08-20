# SyndProxy private pool

## Current pool

- Alive now: 764
- Gold now: 410
- HTTP: 175 alive / 79 gold
- HTTPS: 155 alive / 24 gold
- SOCKS4: 209 alive / 154 gold
- SOCKS5: 225 alive / 153 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26965
- Ever gold: 1090

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
