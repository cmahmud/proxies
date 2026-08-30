# SyndProxy validated proxy pool

## Current pool

- Alive now: 613
- Gold now: 455
- HTTP: 125 alive / 86 gold
- HTTPS: 116 alive / 38 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 206 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44776
- Ever gold: 1413

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
