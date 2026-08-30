# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 443
- HTTP: 116 alive / 81 gold
- HTTPS: 72 alive / 30 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 196 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44592
- Ever gold: 1407

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
