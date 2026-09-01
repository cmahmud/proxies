# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 452
- HTTP: 111 alive / 85 gold
- HTTPS: 128 alive / 31 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 191 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46743
- Ever gold: 1448

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
