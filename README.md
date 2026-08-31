# SyndProxy validated proxy pool

## Current pool

- Alive now: 630
- Gold now: 479
- HTTP: 141 alive / 100 gold
- HTTPS: 112 alive / 43 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 204 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45064
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
