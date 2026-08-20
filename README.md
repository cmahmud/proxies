# SyndProxy private pool

## Current pool

- Alive now: 1162
- Gold now: 568
- HTTP: 423 alive / 193 gold
- HTTPS: 271 alive / 94 gold
- SOCKS4: 240 alive / 146 gold
- SOCKS5: 228 alive / 135 gold

## Historical pool

- Discovered: 136255
- Ever alive: 22865
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
