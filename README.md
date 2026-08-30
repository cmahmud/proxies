# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 487
- HTTP: 147 alive / 102 gold
- HTTPS: 118 alive / 44 gold
- SOCKS4: 169 alive / 163 gold
- SOCKS5: 201 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44981
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
