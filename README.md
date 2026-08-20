# SyndProxy private pool

## Current pool

- Alive now: 1611
- Gold now: 647
- HTTP: 641 alive / 242 gold
- HTTPS: 504 alive / 128 gold
- SOCKS4: 210 alive / 133 gold
- SOCKS5: 256 alive / 144 gold

## Historical pool

- Discovered: 142727
- Ever alive: 24548
- Ever gold: 1027

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
