# SyndProxy validated proxy pool

## Current pool

- Alive now: 693
- Gold now: 465
- HTTP: 144 alive / 94 gold
- HTTPS: 138 alive / 33 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 230 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46179
- Ever gold: 1442

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
