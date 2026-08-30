# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 426
- HTTP: 134 alive / 78 gold
- HTTPS: 51 alive / 22 gold
- SOCKS4: 163 alive / 160 gold
- SOCKS5: 198 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44544
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
