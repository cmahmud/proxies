# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 464
- HTTP: 128 alive / 96 gold
- HTTPS: 112 alive / 37 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 202 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44823
- Ever gold: 1414

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
