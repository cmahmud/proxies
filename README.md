# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 444
- HTTP: 116 alive / 76 gold
- HTTPS: 146 alive / 38 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44667
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
