# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 487
- HTTP: 148 alive / 103 gold
- HTTPS: 117 alive / 44 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 204 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44981
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
