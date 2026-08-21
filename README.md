# SyndProxy private pool

## Current pool

- Alive now: 770
- Gold now: 409
- HTTP: 224 alive / 88 gold
- HTTPS: 128 alive / 20 gold
- SOCKS4: 200 alive / 146 gold
- SOCKS5: 218 alive / 155 gold

## Historical pool

- Discovered: 152161
- Ever alive: 27841
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
