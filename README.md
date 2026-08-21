# SyndProxy private pool

## Current pool

- Alive now: 778
- Gold now: 410
- HTTP: 234 alive / 90 gold
- HTTPS: 131 alive / 20 gold
- SOCKS4: 194 alive / 147 gold
- SOCKS5: 219 alive / 153 gold

## Historical pool

- Discovered: 152161
- Ever alive: 27841
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
