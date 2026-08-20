# SyndProxy private pool

## Current pool

- Alive now: 786
- Gold now: 400
- HTTP: 195 alive / 77 gold
- HTTPS: 173 alive / 21 gold
- SOCKS4: 214 alive / 151 gold
- SOCKS5: 204 alive / 151 gold

## Historical pool

- Discovered: 149514
- Ever alive: 26937
- Ever gold: 1089

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
