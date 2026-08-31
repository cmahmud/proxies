# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 410
- HTTP: 92 alive / 56 gold
- HTTPS: 70 alive / 26 gold
- SOCKS4: 164 alive / 159 gold
- SOCKS5: 191 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45510
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
