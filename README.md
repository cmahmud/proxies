# SyndProxy private pool

## Current pool

- Alive now: 875
- Gold now: 412
- HTTP: 258 alive / 83 gold
- HTTPS: 173 alive / 24 gold
- SOCKS4: 202 alive / 151 gold
- SOCKS5: 242 alive / 154 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28915
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
