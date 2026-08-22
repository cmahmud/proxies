# SyndProxy private pool

## Current pool

- Alive now: 841
- Gold now: 404
- HTTP: 242 alive / 92 gold
- HTTPS: 172 alive / 24 gold
- SOCKS4: 202 alive / 142 gold
- SOCKS5: 225 alive / 146 gold

## Historical pool

- Discovered: 162755
- Ever alive: 31574
- Ever gold: 1161

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
