# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 414
- HTTP: 90 alive / 57 gold
- HTTPS: 70 alive / 25 gold
- SOCKS4: 189 alive / 163 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45503
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
