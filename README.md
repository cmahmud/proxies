# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 445
- HTTP: 124 alive / 79 gold
- HTTPS: 107 alive / 31 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 218 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45379
- Ever gold: 1430

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
