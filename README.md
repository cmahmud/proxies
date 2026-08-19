# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 323
- HTTP: 336 alive / 51 gold
- HTTPS: 204 alive / 10 gold
- SOCKS4: 203 alive / 131 gold
- SOCKS5: 208 alive / 131 gold

## Historical pool

- Discovered: 129233
- Ever alive: 20034
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
