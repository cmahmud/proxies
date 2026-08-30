# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 466
- HTTP: 130 alive / 91 gold
- HTTPS: 120 alive / 41 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44861
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
