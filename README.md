# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 443
- HTTP: 117 alive / 79 gold
- HTTPS: 124 alive / 35 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44730
- Ever gold: 1411

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
