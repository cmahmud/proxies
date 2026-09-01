# SyndProxy validated proxy pool

## Current pool

- Alive now: 653
- Gold now: 480
- HTTP: 143 alive / 98 gold
- HTTPS: 127 alive / 42 gold
- SOCKS4: 185 alive / 164 gold
- SOCKS5: 198 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46948
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
