# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 488
- HTTP: 157 alive / 101 gold
- HTTPS: 127 alive / 44 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 197 alive / 180 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44984
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
