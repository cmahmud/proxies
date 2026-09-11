# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 454
- HTTP: 105 alive / 86 gold
- HTTPS: 43 alive / 30 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 187 alive / 175 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49188
- Ever gold: 1575

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
