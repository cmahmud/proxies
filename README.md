# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 470
- HTTP: 137 alive / 97 gold
- HTTPS: 57 alive / 35 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 193 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49346
- Ever gold: 1578

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
