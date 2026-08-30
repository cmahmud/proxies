# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 425
- HTTP: 136 alive / 77 gold
- HTTPS: 50 alive / 22 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 197 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44544
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
