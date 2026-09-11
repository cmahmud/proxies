# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 420
- HTTP: 91 alive / 66 gold
- HTTPS: 44 alive / 19 gold
- SOCKS4: 191 alive / 164 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48888
- Ever gold: 1568

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
