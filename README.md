# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 424
- HTTP: 127 alive / 84 gold
- HTTPS: 79 alive / 31 gold
- SOCKS4: 159 alive / 151 gold
- SOCKS5: 189 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44071
- Ever gold: 1394

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
