# SyndProxy private pool

## Current pool

- Alive now: 1579
- Gold now: 630
- HTTP: 619 alive / 232 gold
- HTTPS: 498 alive / 118 gold
- SOCKS4: 204 alive / 136 gold
- SOCKS5: 258 alive / 144 gold

## Historical pool

- Discovered: 142729
- Ever alive: 24581
- Ever gold: 1028

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
