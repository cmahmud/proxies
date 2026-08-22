# SyndProxy private pool

## Current pool

- Alive now: 846
- Gold now: 422
- HTTP: 245 alive / 92 gold
- HTTPS: 170 alive / 26 gold
- SOCKS4: 197 alive / 146 gold
- SOCKS5: 234 alive / 158 gold

## Historical pool

- Discovered: 162753
- Ever alive: 31563
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
