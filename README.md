# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 445
- HTTP: 93 alive / 78 gold
- HTTPS: 99 alive / 32 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47347
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
