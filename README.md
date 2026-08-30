# SyndProxy validated proxy pool

## Current pool

- Alive now: 609
- Gold now: 454
- HTTP: 122 alive / 85 gold
- HTTPS: 118 alive / 39 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 205 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44772
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
