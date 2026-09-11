# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 423
- HTTP: 93 alive / 73 gold
- HTTPS: 36 alive / 15 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48939
- Ever gold: 1569

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
