# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 437
- HTTP: 107 alive / 86 gold
- HTTPS: 51 alive / 32 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 179 alive / 161 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49435
- Ever gold: 1583

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
