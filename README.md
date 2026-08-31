# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 476
- HTTP: 163 alive / 102 gold
- HTTPS: 130 alive / 40 gold
- SOCKS4: 164 alive / 160 gold
- SOCKS5: 197 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45212
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
