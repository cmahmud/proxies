# SyndProxy validated proxy pool

## Current pool

- Alive now: 600
- Gold now: 455
- HTTP: 117 alive / 88 gold
- HTTPS: 116 alive / 32 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45658
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
