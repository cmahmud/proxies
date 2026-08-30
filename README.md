# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 425
- HTTP: 116 alive / 77 gold
- HTTPS: 61 alive / 21 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 193 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44534
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
