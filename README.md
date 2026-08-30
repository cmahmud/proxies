# SyndProxy validated proxy pool

## Current pool

- Alive now: 618
- Gold now: 451
- HTTP: 127 alive / 83 gold
- HTTPS: 119 alive / 38 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 205 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44778
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
