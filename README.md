# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 420
- HTTP: 101 alive / 67 gold
- HTTPS: 49 alive / 20 gold
- SOCKS4: 193 alive / 163 gold
- SOCKS5: 197 alive / 170 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48918
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
