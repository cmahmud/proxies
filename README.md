# SyndProxy validated proxy pool

## Current pool

- Alive now: 643
- Gold now: 473
- HTTP: 154 alive / 102 gold
- HTTPS: 124 alive / 36 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 197 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45198
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
