# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 427
- HTTP: 135 alive / 79 gold
- HTTPS: 48 alive / 21 gold
- SOCKS4: 163 alive / 161 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44544
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
