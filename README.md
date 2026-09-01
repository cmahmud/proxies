# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 476
- HTTP: 144 alive / 97 gold
- HTTPS: 118 alive / 39 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 198 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46951
- Ever gold: 1458

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
