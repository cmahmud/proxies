# SyndProxy private pool

## Current pool

- Alive now: 852
- Gold now: 400
- HTTP: 235 alive / 91 gold
- HTTPS: 182 alive / 29 gold
- SOCKS4: 185 alive / 123 gold
- SOCKS5: 250 alive / 157 gold

## Historical pool

- Discovered: 167131
- Ever alive: 32550
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
