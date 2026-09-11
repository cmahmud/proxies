# SyndProxy validated proxy pool

## Current pool

- Alive now: 551
- Gold now: 459
- HTTP: 124 alive / 84 gold
- HTTPS: 54 alive / 33 gold
- SOCKS4: 175 alive / 164 gold
- SOCKS5: 198 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49229
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
