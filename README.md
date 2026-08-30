# SyndProxy validated proxy pool

## Current pool

- Alive now: 636
- Gold now: 487
- HTTP: 145 alive / 102 gold
- HTTPS: 115 alive / 44 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 204 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44981
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
