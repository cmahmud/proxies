# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 480
- HTTP: 159 alive / 99 gold
- HTTPS: 144 alive / 44 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 203 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44968
- Ever gold: 1421

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
